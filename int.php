<?php
interface A
{
    function Display();

}
class B implements A
{
    function Display()
    {
        echo "Implemented method named display called";
    }
}
(new B())->Display();
?>