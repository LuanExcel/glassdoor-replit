
{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.playwright-driver.browsers
    pkgs.chromium
  ];
}
