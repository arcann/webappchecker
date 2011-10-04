package DSS_Password;

require Exporter;
@ISA = qw(Exporter);

############################
#Declare Functions to export
############################

@EXPORT = qw(
  get_id_password
);

############################
#Define Function Bodies
############################

sub get_id_password
{
  my ($target_system) = @_;

  my $id = '';
  my $pwd = '';

  open(ID,"< passwords") 
    or open(ID,"< ~/passwords") 
    or die "Failed to open password file. $!\n" ;
  while(defined( $line = <ID> ))
  {
    chomp($line);
    ($this_system,$this_id,$this_pwd) = split(/ +/,$line);
    if ($this_system eq $target_system)
    {
      $id = $this_id;
      $pwd = $this_pwd;
    }
  }
  close(ID);
  if ($id eq '') 
  {
    die "Didn't find id/password for $target_system\n";
  }

  return $id, $pwd;
}

# Some perls require this
1;
