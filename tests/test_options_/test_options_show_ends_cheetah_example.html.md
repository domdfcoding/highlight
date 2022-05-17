<[94mhtml[39;49;00m>$
  <[94mhead[39;49;00m><[94mtitle[39;49;00m>$title</[94mtitle[39;49;00m></[94mhead[39;49;00m>$
  <[94mbody[39;49;00m>$
    <[94mtable[39;49;00m>$
      #for $client in $clients$
      <[94mtr[39;49;00m>$
        <[94mtd[39;49;00m>$client.surname, $client.firstname</[94mtd[39;49;00m>$
        <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"mailto:$client.email"[39;49;00m>$client.email</[94ma[39;49;00m></[94mtd[39;49;00m>$
      </[94mtr[39;49;00m>$
      #end for$
    </[94mtable[39;49;00m>$
  </[94mbody[39;49;00m>$
</[94mhtml[39;49;00m>$
