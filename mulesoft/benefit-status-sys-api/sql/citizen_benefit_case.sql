-- Demo-only Oracle Autonomous schema for the citizen-service demonstration.
-- This simulates a COBOL/Java legacy system of record.
-- Do not include real citizen data.

create table citizen_benefit_case (
  case_id varchar2(30) primary key,
  citizen_display_name varchar2(120) not null,
  citizen_ref_masked varchar2(40) not null,
  benefit_type varchar2(80) not null,
  status_code varchar2(40) not null,
  missing_document varchar2(120),
  next_deadline date,
  preferred_channel varchar2(30),
  last_updated_at timestamp default systimestamp not null
);

insert into citizen_benefit_case (
  case_id,
  citizen_display_name,
  citizen_ref_masked,
  benefit_type,
  status_code,
  missing_document,
  next_deadline,
  preferred_channel
) values (
  'BEN-2026-004219',
  'Persona Demo A',
  'CIT-****-4219',
  'Benefit renewal',
  'PENDING_DOCUMENT',
  'Proof of residence',
  date '2026-07-05',
  'WhatsApp'
);

insert into citizen_benefit_case (
  case_id,
  citizen_display_name,
  citizen_ref_masked,
  benefit_type,
  status_code,
  missing_document,
  next_deadline,
  preferred_channel
) values (
  'BEN-2026-004227',
  'Persona Demo B',
  'CIT-****-1008',
  'Benefit renewal',
  'ESCALATED_TO_AGENT',
  'Proof of residence',
  date '2026-07-24',
  'Phone'
);

commit;

-- Verification query:
-- select * from citizen_benefit_case where case_id in ('BEN-2026-004219', 'BEN-2026-004227');
