# Puppet file to configure nginx servers to add custom headers to their response

file_line { 'custom_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  match  => 'add_header X-Served-By ',
  line   => "\t\tadd_header X-Served-By ${hostname}",
  after  => 'location / {',
}
