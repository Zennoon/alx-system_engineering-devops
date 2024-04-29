# Puppet file to configure nginx servers to add custom headers to their response

exec { 'update':
  command => 'apt-get update -y; apt-get upgrade-y',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { 'index.nginx-debian.html':
  ensure  => file,
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'add header' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

service { 'nginx':
  ensure => running,
}
