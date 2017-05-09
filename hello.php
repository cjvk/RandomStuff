<?php
echo "Hello world!\n";

interface IPPOT
{
	public function ippot($num);
}
// Implementations under test
$Impls = array();

class Hardcoded1 implements IPPOT
{
	public function ippot($num)
	{
		if (!is_int($num))
		{
			return False;
		}
		$ppots = array(2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,65536);
		return in_array($num, $ppots);
	}
}
array_push($Impls, new Hardcoded1());

function runTests($impls)
{
	$trues = array(2, 4, 8, 16, 32, 64, 65536);
	$falses = array(1, -8, 0, 17, 33, 100);
	$oddballs = array("hello", "", "2", "16");
	foreach($impls as $impl)
	{
		foreach($trues as $t)
		{
			if (!$impl->ippot($t))
			{
				echo $t;
				throw new Exception("should be true: {$t}");
			}
		}
		$combined_falses = array_merge($falses, $oddballs);
		foreach($combined_falses as $f)
		{
			if ($impl->ippot($f))
			{
				throw new Exception('should be false: {$f}');
			}
		}
	}
}

runTests($Impls);

?>
