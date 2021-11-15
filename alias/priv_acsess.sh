
if ! $_isroot; then
  alias sudo='sudo '
  alias scat='sudo cat'
  alias svim='sudoedit'
  alias root='sudo su'
  alias reboot='sudo reboot'
  alias halt='sudo halt'
  alias powertop='sudo powertop'

  # Alias's for safe and forced reboots
  alias rebootsafe='sudo shutdown -r now'
  alias rebootforce='sudo shutdown -r -n now'
fi