# Manifest to fix typo in a word-press php setting file

$fpath = '/var/www/html/wp-settings.php'
exec { 'phpp_to_php':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' ${fpath}",
  path     => '/bin'
} -> service { 'restart_apache2':
  name   => 'apache2',
  ensure => 'running'
}
