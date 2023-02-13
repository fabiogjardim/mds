create table delta.myschema.results
(
  dt varchar 
 ,home_teamName varchar
 ,away_teamName varchar
 ,home_scoreHome varchar 
 ,away_scoreAway varchar 
 ,tournamentName varchar
 ,cityCity varchar
 ,countryCountry varchar
 ,neutralTRUE varchar
)
with
(LOCATION = 's3a://delta-lake/demo2' , checkpoint_interval = 5);


CALL example.system.register_table(schema_name => 'myschema', table_name => 'results', table_location => 's3a://delta-lake/demo2')