# Define a class for configuring Nginx with a custom HTTP header
class custom_http_response_header {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Create a custom fact to get the hostname of the server
  # This fact will be used to set the value of the custom header
  facterng::fact { 'server_hostname':
    value => $::hostname,
  }

  # Configure Nginx with the custom HTTP response header
  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => "add_header X-Served-By $::server_hostname;",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

# Include the custom_http_response_header class
include custom_http_response_header
