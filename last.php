<?php
print "<b>Employee Details</b>";
print "<form method='post'>";
print "Enter id<br><input type = 'text' name = 'id'><br><br>";
print "Enter name<br><input type = 'text' name = 'name'><br><br>";
print "Enter designation<br><input type = 'text' name = 'design'><br><br>";
print "Enter department<br><input type = 'text' name = 'dept'><br><br>";
print "<input type='submit' name='submit'>";
print "</form>";

class Personal{
    public $id;
    public $name;
    public $design;
    public $dept;
    function getDetails(){
        $this->id = $_POST['id'];
        $this->name = $_POST['name'];
        $this->design = $_POST['design'];
        $this->dept = $_POST['dept'];
    }
}
class Company extends Personal{
    function showDetails(){
        return "Id: " . $this->id . "<br>Name: " . $this->name . "<br>Designation: " . $this->design . "<br>Department: " . $this->dept;
    }
}
if(isset($_POST['submit'])){
    $emp = new Company();
    $emp->getDetails();
    print $emp->showDetails();
}
?>

