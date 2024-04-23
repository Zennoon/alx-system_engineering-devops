# Puppet file to configure nginx on a server

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

$newline = "rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"

exec {'redirect':
  command  => "sed -i \"24i\	${newline}\" /etc/nginx/sites-available/default",
  provider => 'shell'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
