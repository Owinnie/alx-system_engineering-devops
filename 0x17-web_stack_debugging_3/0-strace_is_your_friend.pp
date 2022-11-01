# Fix typo -- working with wordpress

exec { 'typo-error':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
