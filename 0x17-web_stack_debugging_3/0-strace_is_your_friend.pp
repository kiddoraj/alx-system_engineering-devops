# Define an 'exec' resource to fix the 'phpp' extensions in wp-settings.php
exec { 'fix-wordpress':
  # The title uniquely identifies this resource
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  
  # Specify the command to be executed
  # This 'sed' command replaces 'phpp' with 'php' globally in the specified file
  # '-i' flag indicates an in-place edit
  path    => '/usr/local/bin/:/bin/',
}
