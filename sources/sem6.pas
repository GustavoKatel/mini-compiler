program Program;
    var int1: integer;
        real1: real;
begin
    if (int1 >= 20) then
        int1 := 2;

    if (int1 >= 20) and (real1 <= 90) then
        real1 := 2.2;

    if (int1 >= 20.5) or (real1 <= (90 + 5)) then
        real1 := 2.2
end.
