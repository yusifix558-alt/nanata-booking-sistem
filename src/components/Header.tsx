"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

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
      className={`fixed w-full max-w-[430px] top-0 z-50 transition-colors duration-300 ${
        scrolled ? "bg-paper border-b border-dark/10" : "bg-transparent border-b border-dark"
      }`}
    >
      <div className="flex justify-between items-center px-6 py-4">
        {/* Center: Logo */}
        <Link href="/" className="font-editorial text-2xl tracking-normal normal-case italic font-semibold text-dark flex-1 text-left">
          Namata Studio<span className="text-namata-pink">.</span>
        </Link>

        {/* Mobile Nav Toggle */}
        <button
          className="p-2 text-dark"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          aria-label="Toggle Menu"
        >
          {isMobileMenuOpen ? (
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          ) : (
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1" strokeLinecap="round" strokeLinejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
          )}
        </button>
      </div>

      {/* Mobile Nav Drawer */}
      {isMobileMenuOpen && (
        <div className="absolute top-[100%] left-0 w-full h-screen bg-paper flex flex-col items-center pt-16 space-y-10 z-40 border-t border-dark">
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
