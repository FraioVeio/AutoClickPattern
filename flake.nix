{
  description = "A Nix-flake-based Python development environment for screenshot matching";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
  };

  outputs = { self , nixpkgs ,... }: let
    # system should match the system you are running on
    system = "x86_64-linux";  # Cambia in base alla tua architettura (x86_64-darwin per macOS)
  in {
    devShells."${system}".default = let
      pkgs = import nixpkgs {
        inherit system;
      };
    in pkgs.mkShell {
      # Dipendenze per il tuo progetto Python
      packages = with pkgs; [
        python310Full
        python310Packages.pyautogui
        python310Packages.opencv4
        python310Packages.pillow
        python310Packages.numpy
        scrot
      ];

      shellHook = ''
        echo "Benvenuto nell'ambiente Python con tutte le dipendenze installate!"
      '';
    };
  };
}
