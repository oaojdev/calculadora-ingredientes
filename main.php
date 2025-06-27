<?php

$array = ("a" => 2, "b" => 8, "c" => 42);
$var1 = $array["a"] + $array["c"];
$var2 = $var1 + $var1;
$var3 = $var2/ $array["b"];

echo($var3)