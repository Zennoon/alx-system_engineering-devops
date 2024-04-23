package { 'nginx':
  name     => 'nginx',
  provider => 'apt',
}

file { 'index.nginx-debian.html':
  ensure  => file,
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}

$newline = 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'

file_line { 'redirect':
  line => "server_name _;\n\t${newline}",
  match => 'server_name _;',
  replace => true,
}
