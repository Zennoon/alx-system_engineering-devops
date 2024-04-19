# Puppet manifest that kills a process called 'killmenow'

exec { 'kill_process':
  command => 'pkill killmenow',
  path => '/usr/bin'
}
