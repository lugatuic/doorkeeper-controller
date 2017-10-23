<?php

$uin = (isset($_POST['UIN'])) ? $_POST['UIN'] : 0;
// Replace the array with your list of allowable ids.
$allowable = ['00000000'];

if (in_array($uin, $allowable)) {
	echo "1";
} else {
	echo "0";
}

?>
