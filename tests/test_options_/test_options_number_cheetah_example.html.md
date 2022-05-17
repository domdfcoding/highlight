     1	<[94mhtml[39;49;00m>
     2	  <[94mhead[39;49;00m><[94mtitle[39;49;00m>$title</[94mtitle[39;49;00m></[94mhead[39;49;00m>
     3	  <[94mbody[39;49;00m>
     4	    <[94mtable[39;49;00m>
     5	      #for $client in $clients
     6	      <[94mtr[39;49;00m>
     7	        <[94mtd[39;49;00m>$client.surname, $client.firstname</[94mtd[39;49;00m>
     8	        <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"mailto:$client.email"[39;49;00m>$client.email</[94ma[39;49;00m></[94mtd[39;49;00m>
     9	      </[94mtr[39;49;00m>
    10	      #end for
    11	    </[94mtable[39;49;00m>
    12	  </[94mbody[39;49;00m>
    13	</[94mhtml[39;49;00m>
