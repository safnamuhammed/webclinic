<?php
print "<b>Addition</b><br><br>";
print "<form method='post'>";

print "Enter a SAFNA <br><input type='number' name='num1'><br><br>";
print "Enter another number<br><input type='text' name='num2'><br><br>";

print "<input type='submit' value='Submit' name='add'>";

print "</form>";

if (isset($_POST['add'])) {
    $obj = new X();
    $obj->get();
    $obj->display();
}
class x
{
    public $x, $y, $z;
    function get()
    {
        $this->x = $_POST['num1'];
        $this->y = $_POST['num2'];
        $this->z = $this->x + $this->y;
    }
    function display()
    {
        echo "<br>Result = " . $this->z;
    }
}