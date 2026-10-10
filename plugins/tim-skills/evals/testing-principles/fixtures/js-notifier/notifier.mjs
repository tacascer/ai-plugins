// Requirement: one welcome message for a newly registered user.
export function welcome(address, sender) {
  sender.send(address, 'Welcome');
  sender.send(address, 'Welcome');
}
