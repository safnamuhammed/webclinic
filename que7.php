<?php

function greatestAge($age1, $age2)
{
    if($age1 > $age2)
    {
        return $age1;
    }
    else
    {
        return $age2;
    }
}

print "<b>FIND THE GREATEST AGE</b><br><br>";

print "<form method='post'>";

print "Enter Age of Person 1:<br>";
print "<input type='number' name='age1' required><br><br>";

print "Enter Age of Person 2:<br>";
print "<input type='number' name='age2' required><br><br>";

print "<input type='submit' name='check' value='Find Greatest Age'>";

print "</form>";

if(isset($_POST['check']))
{
    $age1 = $_POST['age1'];
    $age2 = $_POST['age2'];

    $result = greatestAge($age1, $age2);

    print "<br><b>Greatest Age is: $result</b>";
}

?>