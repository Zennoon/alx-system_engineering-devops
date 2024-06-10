# Manifest to increase nginx's limit of open files to be able to handle more
# concurrent connections

exec { 'increase-limit':
  notify  => Service['restart-nginx'],
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => '/bin'
}

service { 'restart-nginx':
  ensure => 'running',
  name   => 'nginx'
}
