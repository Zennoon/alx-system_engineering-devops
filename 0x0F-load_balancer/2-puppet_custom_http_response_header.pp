# Puppet file to configure nginx servers to add custom headers to their response

exec { 'custom_header':
  command => 'sudo sed -i "s/location \/ {/location \/ {\n\t\tadd_header X-Served-By $(hostname);/" /etc/nginx/sites-available/default',
    path  => '/usr/bin'
}
