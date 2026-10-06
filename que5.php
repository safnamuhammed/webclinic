<?php

function isPrime($num)
{
    if($num < 2)
        return false;

    for($i = 2; $i <= $num/2; $i++)
    {
        if($num % $i == 0)
            return false;
    }

    return true;
}



    print "<form method='post'>";
    print "<b>PRIME NUMBERS IN AN ARRAY</b><br><br>";
    print "Enter the size of the array:<br>";
    print "<input type='number' name='size' required><br><br>";
    print "<input type='submit' name='create' value='Create Array'>";
    print "</form>";



if(isset($_POST['create']))
    {
    $size = $_POST['size'];

    print "<form method='post'>";

    for($i = 0; $i < $size; $i++)
    {
        print "Enter Element ".($i+1).": ";
        print "<input type='number' name='arr[]' required><br><br>";
    }

    print "<input type='submit' name='find' value='Find Prime Numbers'>";
    print "</form>";
    }


if(isset($_POST['find']))
{
    $arr = $_POST['arr'];

    print "<b>Prime Numbers are:</b><br><br>";

    foreach($arr as $num)
    {
        if(isPrime($num))
        {
            print $num."<br>";
        }
    }
}

?>