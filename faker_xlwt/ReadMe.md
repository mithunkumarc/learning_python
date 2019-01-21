xlwt : writing data to excel file : 

        import xlwt  # excel 
        import faker

        # fake data
        data = faker.Faker()

        # creating workbook
        wb = xlwt.Workbook()

        # worksheet
        ws = wb.add_sheet('A Test Sheet')

        #heading 
        # write(row, col, data)
        ws.write(0, 0, "name")
        ws.write(0, 1, "email")

        # data from first row
        for i in range(1,10):
            ws.write(i,0,data.name())
            ws.write(i,1,data.email())    


        wb.save('example.xls')
        
        
xlrd : reading excel file

        import xlrd
        book=xlrd.open_workbook('example.xls')
        sheet=book.sheet_by_index(0)
        #print(sheet)
        #dir(sheet)
        print(sheet.cell(0,0).value+'\t'+sheet.cell(0,1).value)
        # print(sheet.nrows)
        # print(sheet.ncols)
        for i in range(1,sheet.nrows):
            for j in range(0,sheet.ncols):
                print(sheet.cell(i,j).value+'\t')
            print('\n')
