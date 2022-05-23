first_name = " larry   "
last_name = "   holedigger  "
full_name = f"{first_name} {last_name}"

print(full_name)

rstrip = full_name.rstrip()
print(rstrip)

lstrip = full_name.lstrip()
print(lstrip)

strip = full_name.strip()
print(strip)

first_name_strip = first_name.strip()
last_name_strip = last_name.strip()
full_name_strip = f"{first_name_strip} {last_name_strip}"
print(full_name_strip.title())

# It appears that you need to strip raw data,
# and not operating on 'f' (full_name in this case).
