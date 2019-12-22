{ pkgs ? import <nixpkgs> { } }:
pkgs.stdenv.mkDerivation rec {
  src = ./.;
  version = "1.0.0";
  buildInputs = with pkgs; [ discord makeWrapper ];
  name = "betterdiscordctl-${version}";
  installPhase = ''
    mkdir -p $out/bin

    cp betterdiscordctl $out/bin/
    chmod +x $out/bin/betterdiscordctl
    wrapProgram $out/bin/betterdiscordctl --add-flags "--nix"
  '';
  postInstall = ''
    wrapProgram $out/bin/betterdiscordctl
  '';
}
