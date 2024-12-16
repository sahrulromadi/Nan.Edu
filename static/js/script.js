$(document).ready(function () {
  // NAVBAR
  (function setupNavbarOpacity() {
    $(window).on("scroll", function () {
      const navbar = $("header");
      navbar.css("opacity", $(this).scrollTop() > 5 ? "0.9" : "1");
    });
  })();

  // FORM VALIDATION
  (function setupFormValidation() {
    $(".needs-validation").on("submit", function (event) {
      if (!this.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      $(this).addClass("was-validated");
    });
  })();

  // SCROLL TO TOP
  (function setupScrollToTop() {
    const $scrollToTop = $("#scrollToTop");
    $(window).on("scroll", function () {
      $(this).scrollTop() > 250
        ? $scrollToTop.removeClass("d-none")
        : $scrollToTop.addClass("d-none");
    });

    $scrollToTop.on("click", function () {
      $("html, body").animate({ scrollTop: 0 }, "fast");
    });
  })();

  // FAQ
  (function setupFaqToggle() {
    $(".faq-item").on("click", function () {
      const $answer = $(this).find(".faq-answer");
      const $icon = $(this).find(".faq-question i");
      $answer.slideToggle();
      $icon.toggleClass("bi-plus bi-dash");
    });
  })();

  // FORM ERROR MODAL
  (function setupFormErrors() {
    if ($("#formErrors").data("errors")) {
      const myModal = new bootstrap.Modal(
        document.getElementById("exampleModal")
      );
      myModal.show();
    }
  })();

  // PROFILE PHOTO
  (function setupProfilePhoto() {
    const initialImageSrc = $("#profile-photo-preview").attr("src");

    $("#profile-photo-input").on("change", function (event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          $("#profile-photo-preview").attr("src", e.target.result);
        };
        reader.readAsDataURL(file);
      }
    });

    $("#clearBtn").on("click", function () {
      $(this).closest("form")[0].reset();
      $("#profile-photo-preview").attr("src", initialImageSrc);
    });
  })();

  // Fungsi slider dinamis
  function setupSlider(sliderId, prevBtnId, nextBtnId) {
    let currentIndex = 0;

    // Ambil elemen slider dan card
    const $sliderRow = $(`#${sliderId} .slider-row`);
    const $slider = $(`#${sliderId}`);
    const $cards = $sliderRow.find(".col-12");

    // Hitung ukuran card dan jumlah maksimal index
    const updateSliderConfig = () => {
      const cardWidth = $cards.outerWidth(true);
      const visibleCards = Math.floor($slider.outerWidth() / cardWidth);
      return {
        cardWidth,
        maxIndex: $cards.length - visibleCards,
      };
    };

    let { cardWidth, maxIndex } = updateSliderConfig();

    // Fungsi untuk geser ke kanan
    function slideNext() {
      currentIndex = currentIndex < maxIndex ? currentIndex + 1 : 0; // Reset jika sudah di akhir
      $sliderRow.css("transform", `translateX(-${currentIndex * cardWidth}px)`);
    }

    // Fungsi untuk geser ke kiri
    function slidePrev() {
      currentIndex = currentIndex > 0 ? currentIndex - 1 : maxIndex; // Reset ke akhir jika di awal
      $sliderRow.css("transform", `translateX(-${currentIndex * cardWidth}px)`);
    }

    // Event tombol
    $(`#${nextBtnId}`).click(slideNext);
    $(`#${prevBtnId}`).click(slidePrev);

    // Update konfigurasi saat window di-resize
    $(window).resize(() => {
      const config = updateSliderConfig();
      cardWidth = config.cardWidth;
      maxIndex = config.maxIndex;
      currentIndex = Math.min(currentIndex, maxIndex); // Pastikan index tidak lebih dari maxIndex
      $sliderRow.css("transform", `translateX(-${currentIndex * cardWidth}px)`);
    });
  }

  // Inisialisasi slider
  $(document).ready(function () {
    setupSlider("news-slider", "prev-news-btn", "next-news-btn");
    setupSlider("course-slider", "prev-course-btn", "next-course-btn");
  });

  // CHANGE EMAIL
  (function setupChangeEmail() {
    $(".add-email").on("click", function () {
      $(".change-email-form").toggleClass("d-none d-block");
    });
  })();

  // PAYMENTS
  (function setupPayments() {
    const bankAccounts = {
      BRI: "1234 5678 9101 1121 (a/n NAN.EDU BRI)",
      BNI: "2345 6789 1011 2233 (a/n NAN.EDU BNI)",
      Mandiri: "3456 7890 1121 3344 (a/n NAN.EDU Mandiri)",
      BCA: "4567 8901 2233 4455 (a/n NAN.EDU BCA)",
    };

    $("#paymentMethod").on("change", function () {
      const paymentMethod = $(this).val();
      const $bankInfo = $("#bankInfo");
      const $bankAccount = $("#bankAccount");

      if (bankAccounts[paymentMethod]) {
        $bankInfo.show();
        $bankAccount.text(`Nomor Rekening: ${bankAccounts[paymentMethod]}`);
      } else {
        $bankInfo.hide();
        $bankAccount.text("");
      }
    });

    $("#paymentProof").on("change", function (event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          $("#previewImage").attr("src", e.target.result);
          $("#imagePreview").addClass("d-flex").removeClass("d-none");
        };
        reader.readAsDataURL(file);
      } else {
        $("#imagePreview").addClass("d-none").removeClass("d-flex");
      }
    });
  })();
});
