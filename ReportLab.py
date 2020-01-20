from reportlab.pdfgen import canvas
aux = canvas.Canvas("proba.pdf")
aux.drawString(0, 0, "Posición (x,y) = (0,0)")
aux.drawString(50, 100, "Posición (x,y) = (50,100)")
aux.drawString(150, 50, "Posición (x,y) = (150,50)")
aux.drawImage("hackerman.png", 0, 0)
aux.showPage()
aux.save()