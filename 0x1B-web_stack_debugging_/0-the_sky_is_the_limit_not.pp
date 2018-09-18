# fix max open file limit error
exec {'increase max open files limit':
  command => 'sed -i "s|15|15000|g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}

exec {'restart nginx':
  require => Exec['increase max open files limit'],
  command => 'sudo service nginx restart',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}
