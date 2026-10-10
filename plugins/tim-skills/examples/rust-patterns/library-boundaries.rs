//! Original example: a borrowed text boundary and safe partial progress.
use std::borrow::Cow;

pub fn display_text(bytes: &[u8]) -> Cow<'_, str> {
    String::from_utf8_lossy(bytes)
}

pub trait Accepts {
    fn accepts(&self, text: &str) -> bool;
}

// Supports either a concrete implementation or a borrowed trait object.
pub fn accepted_by<A: Accepts + ?Sized>(rule: &A, bytes: &[u8]) -> bool {
    rule.accepts(&display_text(bytes))
}

// Contract: keep successful additions if the producer returns None or unwinds.
// push maintains initialized length, avoiding a manual set_len obligation.
pub fn append_available<T>(out: &mut Vec<T>, limit: usize, mut next: impl FnMut() -> Option<T>) {
    for _ in 0..limit {
        match next() {
            Some(value) => out.push(value),
            None => break,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    struct Nonempty;
    impl Accepts for Nonempty {
        fn accepts(&self, text: &str) -> bool { !text.is_empty() }
    }

    #[test]
    fn valid_text_borrows_input() {
        let input = b"packet";
        let result = display_text(input);
        assert!(matches!(result, Cow::Borrowed("packet")));
        assert_eq!(result.as_ptr(), input.as_ptr());
    }

    #[test]
    fn invalid_text_allocates_without_consuming_input() {
        let input = vec![b'a', 0xff];
        let result = display_text(&input);
        assert!(matches!(result, Cow::Owned(_)));
        assert_eq!(result, "a\u{fffd}");
        assert_eq!(input, [b'a', 0xff]);
    }

    #[test]
    fn both_dispatch_forms_preserve_behavior() {
        let concrete = Nonempty;
        let erased: &dyn Accepts = &concrete;
        assert!(accepted_by(&concrete, b"packet"));
        assert!(accepted_by(erased, b"packet"));
        assert!(!accepted_by(erased, b""));
    }

    #[test]
    fn early_stop_keeps_only_produced_values() {
        let mut out = vec![10];
        let mut source = [20, 30].into_iter();
        append_available(&mut out, 8, || source.next());
        assert_eq!(out, [10, 20, 30]);
        append_available(&mut out, 0, || panic!("zero limit must not call producer"));
        assert_eq!(out, [10, 20, 30]);
    }

    #[test]
    fn unwind_preserves_initialized_values_and_drops_them_once() {
        use std::cell::Cell;
        use std::rc::Rc;
        struct CountDrop(Rc<Cell<usize>>);
        impl Drop for CountDrop {
            fn drop(&mut self) { self.0.set(self.0.get() + 1); }
        }
        let drops = Rc::new(Cell::new(0));
        let mut out = Vec::new();
        let mut calls = 0;
        let result = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
            append_available(&mut out, 4, || {
                calls += 1;
                if calls == 3 { panic!("producer failed"); }
                Some(CountDrop(Rc::clone(&drops)))
            });
        }));
        assert!(result.is_err());
        assert_eq!(out.len(), 2);
        assert_eq!(drops.get(), 0);
        drop(out);
        assert_eq!(drops.get(), 2);
    }
}
