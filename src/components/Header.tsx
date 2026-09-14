"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Menu, X } from "lucide-react";

export default function Header() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    handleScroll();
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const navLinks = [
    { name: "HOME", href: "/" },
    { name: "TREATMENTS", href: "/#treatments" },
    { name: "ARTISTS", href: "/#artists" },
  ];

  return (
    <header 
      className={`fixed w-full top-0 z-50 transition-colors duration-300 ${
        scrolled ? "bg-paper border-b border-dark/10" : "bg-transparent border-b border-dark"
      }`}
    >
      <div className="flex justify-between items-center px-6 py-4">
        {/* Left: Est */}
        <div className="hidden lg:block w-32 uppercase tracking-[0.2em] text-[10px] font-medium text-dark/60">
          Est. 2024
        </div>

        {/* Center: Logo */}
        <Link href="/" className="font-editorial text-2xl tracking-normal normal-case italic font-semibold text-dark flex-1 lg:flex-none text-left lg:text-center">
          Namata Studio<span className="text-namata-pink">.</span>
        </Link>

        {/* Right: Desk Nav */}
        <div className="hidden lg:flex items-center space-x-8 w-auto">
          <nav className="flex items-center space-x-8">
            {navLinks.map((link) => (
              <Link
                key={link.name}
                href={link.href}
                className="uppercase tracking-[0.2em] text-[10px] font-medium text-dark/70 hover:text-namata-pink transition-colors"
              >
                {link.name}
              </Link>
            ))}
          </nav>
          <Link
            href="/booking"
            className="uppercase tracking-[0.2em] text-[10px] font-bold text-dark border-b border-dark pb-0.5 hover:text-namata-pink hover:border-namata-pink transition-colors"
          >
            Booking
          </Link>
        </div>

        {/* Mobile Nav Toggle */}
        <button
          className="lg:hidden p-2 text-dark"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          aria-label="Toggle Menu"
        >
          {isMobileMenuOpen ? <X size={24} strokeWidth={1} /> : <Menu size={24} strokeWidth={1} />}
        </button>
      </div>

      {/* Mobile Nav Drawer */}
      {isMobileMenuOpen && (
        <div className="lg:hidden absolute top-[100%] left-0 w-full h-screen bg-paper flex flex-col items-center pt-16 space-y-10 z-40 border-t border-dark">
          {navLinks.map((link) => (
            <Link
              key={link.name}
              href={link.href}
              className="text-lg font-editorial font-medium tracking-[0.2em] text-dark hover:text-namata-pink transition-colors uppercase"
              onClick={() => setIsMobileMenuOpen(false)}
            >
              {link.name}
            </Link>
          ))}
          <Link
            href="/booking"
            className="text-[11px] font-bold tracking-[0.2em] text-paper bg-dark px-10 py-4 mt-8 uppercase"
            onClick={() => setIsMobileMenuOpen(false)}
          >
            BOOKING
          </Link>
        </div>
      )}
    </header>
  );
}
