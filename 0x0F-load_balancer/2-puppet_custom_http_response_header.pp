# Puppet file to configure nginx servers to add custom headers to their response

exec { 'update':
  command => 'apt-get update -y; apt-get upgrade -y',
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

exec { 'custom_header':
  command => 'sudo sed -i "s/location \/ {/location \/ {\n\t\tadd_header X-Served-By $(hostname);/" /etc/nginx/sites-available/default',
    path  => '/usr/bin',
}

service { 'nginx':
  ensure => running,
}
