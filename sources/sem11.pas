program Program;
    var int1: integer;

    procedure proc1(int1: integer);
    begin
        proc2(2)
    end;

    procedure proc2(int1: integer);
    begin
        proc1(1)
    end;
begin
    int1 := 2
end.
