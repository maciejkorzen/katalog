#!/bin/sh
# Katalog by Maciej Korzen <maciek@korzen.org>
#
#    Copyright (C) 2001-2003  Maciej Korzen
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

# <SETTINGS>
katsch="/usr/local/bin/katsch"
data="/tmp/katalog"
nice="/usr/bin/nice"
# </SETTINGS>

echo -e "Content-Type: text/html\n"
echo "<html><head></head><body>"

search="`echo \"$QUERY_STRING\" | egrep '^search=' | cut -d '=' -f 2 | sed 's,+, ,g' | sed 's,%2F,/,g'`"

cat << EOF
<H2>Katalog WWW frontend</H2>
<FORM action="./katalog.cgi">
EOF

if [ "x$search" = "x" ]; then

cat << EOF
Search: <input name="search">
<input type="submit">
</form>
EOF

else

cat << EOF
Search: <input name="search" value="$search">
<input type="submit">
</form>
<hr>
EOF

  "$nice" -n 20 "$katsch" -c off -v off -d off -w on -k "$data" "$search"
  echo "<hr>"
fi

echo "</body></html>"
