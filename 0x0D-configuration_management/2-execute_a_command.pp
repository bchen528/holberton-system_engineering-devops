# kills a process
exec {'killprocess':
  command  => 'pkill killmenow',
  provider => 'shell'
}
