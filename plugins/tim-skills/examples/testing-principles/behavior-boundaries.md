# Behavior and boundary contrasts

The pseudocode uses no framework-specific syntax. Read each example relative to its declared client and boundary.

## One behavior across several classes

`Checkout` asks a `DiscountPolicy` for an eligible discount and uses `Money` to calculate the total.

```text
test "preferred customers receive ten percent off":
  checkout = Checkout(DiscountPolicy(), MoneyRules())

  total = checkout.total(customer = preferred, basket = [item(price = 100)])

  assert total == 90
```

This can be a unit test under the classical definition even though it executes three production classes. The unit is the pricing behavior. If it is fast and its objects are private to the test, it is isolated from other tests. Replacing `DiscountPolicy` merely to keep one class real would narrow the exercised behavior and could couple the test to internal collaboration.

Classification is conditional when `MoneyRules` hides a shared rate table or remote lookup. If each test owns that state and observed execution is fast, unit remains supported. If tests share mutable rates, or if the path is not fast, classify it as integration. Inspect construction, fixtures, and runtime evidence to resolve the branch.

## Getter assertion versus pricing behavior

```text
test "setting percentage stores percentage":
  discount = Discount()
  discount.percentage = 10
  assert discount.percentage == 10
```

This state assertion repeats a trivial assignment. It has little evidence of detecting a meaningful fault.

```text
test "ten percent discount reduces a one-hundred total to ninety":
  price = Pricing(Discount(percentage = 10)).total(100)
  assert price == 90
```

This output assertion protects a pricing rule at the `Pricing` client boundary. It would detect faults in applying the percentage. The comparison is about value, not scope: both tests may be units.

If `percentage` itself is part of a user-visible configuration contract with validation or normalization, the first assertion may protect meaningful behavior. Without that requirement, report its value as conditional rather than inventing one.

## Observable public state versus a leaked cache

```text
test "approved order exposes approved status":
  order = pending_order()
  order.approve()
  assert order.status == APPROVED
```

Although state-based, this assertion observes a domain outcome used by an order client.

```text
test "approval stores the order in cache slot 7":
  order = pending_order()
  order.approve()
  assert order.debug_cache[7] == APPROVED
```

The cache is public in syntax but replaceable at the order boundary. The assertion leaks storage layout and is likely to fail during a behavior-preserving refactor.

If external clients directly consume `debug_cache` under a compatibility promise, it is observable at that wider system boundary despite the name. Inspect consumers and documentation. If that promise is unknown, report both classifications and the missing ownership or compatibility fact.
