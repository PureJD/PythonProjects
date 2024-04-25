import qrcode

EXIT_TERMS = ['quit', 'exit', 'stop']

loop = True
while loop:
    print('''

                  (
 Lets Make QR Codes!
              (   ()   )
    ) ________    //  )
 ()  |\       \  //
 ( \\__ \ ______\//
   \__) |       |
     |  |       |
      \ |       |
       \|_______|
       //    \\
      ((     ||
        \\    ||
     ( ()    ||
      (      () ) )
''')
    selection = str(input('Please add the URL or message you wish to add to your code: '))
    if selection.lower() in EXIT_TERMS:
        loop = False
        break
    image = qrcode.make(selection)
    type(image)
    image.save(f'generated_codes/{selection}.png')

  