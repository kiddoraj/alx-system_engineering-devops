# Enable the user holberton to login and open files without error.
# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['reload-login-shell'],
}

# Reload login shell for changes to take effect
exec { 'reload-login-shell':
  command     => 'su - holberton -c "exec $SHELL"',
  path        => '/usr/local/bin/:/bin/',
  refreshonly => true,
}
