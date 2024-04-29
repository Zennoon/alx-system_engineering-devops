# Puppet file to configure nginx servers to add custom headers to their response

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

$newline = 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'

file_line { 'redirect':
  line    => "server_name _;\n\t${newline}",
  match   => 'server_name _;',
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
}

file_line { 'custom_header':
  ensure  => present,
  line    => "\t\tadd_header X-Served-By ${hostname}",
  after   => '\n\tlocation / {',
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin',
  require => Package['nginx'],
}
