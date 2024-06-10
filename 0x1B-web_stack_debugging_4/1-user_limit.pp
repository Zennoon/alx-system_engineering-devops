# Manifest to increase the max amount of open files for the holberton user

$cmd_hard = 's/holberton hard nofile 5/holberton hard nofile 1000000/'
$file_name = '/etc/security/limits.conf'

exec { 'increase-hard-limit':
  command => "sed -iE '${cmd_hard}' ${file_name}",
  path    => '/bin'
}

$cmd_soft = 's/holberton soft nofile 4/holberton soft nofile 10000/'

exec { 'increase-soft-limit':
  command => "sed -iE '${cmd_soft}' ${file_name}",
  path    => '/bin'
}
