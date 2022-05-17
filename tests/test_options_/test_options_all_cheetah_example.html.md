     1^I<[94mhtml[39;49;00m>$
     2^I  <[94mhead[39;49;00m><[94mtitle[39;49;00m>$title</[94mtitle[39;49;00m></[94mhead[39;49;00m>$
     3^I  <[94mbody[39;49;00m>$
     4^I    <[94mtable[39;49;00m>$
     5^I      #for $client in $clients$
     6^I      <[94mtr[39;49;00m>$
     7^I        <[94mtd[39;49;00m>$client.surname, $client.firstname</[94mtd[39;49;00m>$
     8^I        <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"mailto:$client.email"[39;49;00m>$client.email</[94ma[39;49;00m></[94mtd[39;49;00m>$
     9^I      </[94mtr[39;49;00m>$
    10^I      #end for$
    11^I    </[94mtable[39;49;00m>$
    12^I  </[94mbody[39;49;00m>$
    13^I</[94mhtml[39;49;00m>$
