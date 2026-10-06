<?php
class x
{
    public $a,$b,$c;
    function get(){
        $this->a=30;
        $this->b=40;
        $this->c=$this->a+$this->b;

    }
    function display(){
        echo "<br>Result= ".$this->c;
    }
}

$obj=new x();
$obj->get();
$obj->display();
?>
