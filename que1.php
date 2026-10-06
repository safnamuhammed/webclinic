<?php
print "<b>LARGEST OF THREE NUMBERS</b><br><br>";
print "<form method='post'>";

print "Enter 1st number<br><input type='number' name='n1'><br><br>";
print "Enter 2nd number<br><input type='number' name='n2'><br><br>";
print "Enter 3rd number<br><input type='number' name='n3'><br><br>";

print "<input type='submit' value='Submit' name='check'>";

print "</form>";
if (isset($_POST['check'])) {
 $n1= $_POST['n1'];
 $n2= $_POST['n2'];
 $n3= $_POST['n3'];

 if($n1 > $n2 && $n1 > $n3)
    {
       print "$n1 IS THE LARGEST<br><br>"; 
    }
    elseif($n2 > $n3 && $n2 > $n1)
        {
            print "$n2 IS THE LARGEST<br><br>";
        }
    else
        {
print "$n3 IS THE LARGEST<br><br>";    
        }

}