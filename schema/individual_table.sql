CREATE TABLE IF NOT EXISTS public.individual(
	individual_id serial primary key,
	first_name TEXT NOT NULL,
	middle_name TEXT,
	last_name TEXT,
	phone TEXT,
	address TEXT NOT NULL
)