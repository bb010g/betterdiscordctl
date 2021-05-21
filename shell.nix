{ nixpkgs ? import <nixpkgs> { } }:

nixpkgs.mkShell {
  name = "bb010g-betterdiscordctl-shell";

  # inputsFrom = [ ];
  nativeBuildInputs = [
    nixpkgs.shellcheck
  ];
  buildInputs = [
    nixpkgs.bashInteractive
  ];
}
