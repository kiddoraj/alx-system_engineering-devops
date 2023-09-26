# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx is running
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80 and respond with "Hello World!"
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Enable a 301 redirect at /redirect_me
file { '/etc/nginx/sites-available/redirect_me':
  ensure => file,
  content => template('nginx/redirect_me.erb'),
  require => Package['nginx'],
  notify => Service['nginx'],
  before => File['/etc/nginx/sites-enabled/redirect_me'],
}

file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
  notify => Service['nginx'],
}

# Define a template for the default Nginx site
file { '/var/www/html/index.html':
  ensure => file,
  content => '<html><body>Hello World!</body></html>',
  require => Package['nginx'],
  notify => Service['nginx'],
}
