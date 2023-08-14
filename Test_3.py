from windows_toasts import WindowsToaster, ToastText1
wintoaster = WindowsToaster('Python')
newToast = ToastText1()
newToast.SetBody('Hello, world!')
wintoaster.show_toast(newToast)