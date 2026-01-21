select
    client_id,
    count(distinct donor_id) as total_donors,
    sum(case when gave_last_year = true then 1 else 0 end)::float / count(*) as retention_rate
from raw_donations
group by client_id